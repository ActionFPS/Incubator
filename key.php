<?php

  function match_tag($user, $tag) {
    $tag = str_replace('[', '\[', $tag);
    $tag = str_replace(']', '\]', $tag);
    if(fnmatch($tag, $user['nickname']['nickname'])) return true;
      // if(isset($user['previousNicknames'])) {
      //   foreach($user['previousNicknames'] as $nick) if(fnmatch($tag, $nick['nickname'])) return true;
      // }
    return false;
  }

  function match_group($user, $group) {
    if(isset($group['tags'])) {  foreach($group['tags'] as $tag) if(match_tag($user, $tag)) return true; }
    if(isset($group['tag'])) return match_tag($user, $group['tag']);
  }

  function create_key() {
    $user = $GLOBALS['user'];
    $group = $GLOBALS['groups'];

    @unlink('key');
    @unlink('key.pub');
    @unlink('key.pem');
    @unlink('pubkey.pem');

    exec("ssh-keygen -t dsa -f ./key -N ''");
    exec("openssl dsa -in key -outform pem > key.pem");
    exec('openssl dsa -in key.pem -pubout -out pubkey.pem');

    $key = base64_encode(file_get_contents('pubkey.pem'));
    $line = "id={$GLOBALS['id']} name={$user['user']['nickname']['nickname']}";
    foreach($user['groups'] as $group) {
      $line .= " group=$group";
    }
    $line .= " pubkey=$key"."\n";

    echo '<a href="actionfps://authkey='.base64_encode(file_get_contents('key.pem')).'&authid='.$GLOBALS['id'].'">Add your key</a>';

    return $line;
  }

  function replace_a_line($data) {
    if (stristr($data, 'id='.$GLOBALS['id'].' ')) {
      $GLOBALS['replaced'] = true;
      return create_key();
    }
  return $data;
  }

  function update_groups() {
    $groups = json_decode(file_get_contents('https://actionfps.com/clans/?format=json'), true);
    $fp = fopen('groups.txt', "w+");
    foreach($groups as $group) {
    fwrite($fp, "id={$group['id']} name={$group['name']}\n");
    }
  fclose($fp);
  return 0;
  }

  update_groups();

$_GET['id'] = 'drakas';
  if(isset($_GET['id'])) {

    $id = $_GET['id'];

    if(get_headers('https://actionfps.com/player/?id='.$id.'&format=json')[0] == 'HTTP/1.1 404 Not Found') exit('User does not exist');
    $user = json_decode(file_get_contents('https://actionfps.com/player/?id='.$id.'&format=json'), true);
    $groups = json_decode(file_get_contents('https://actionfps.com/clans/?format=json'), true);

    //get user's groups
    $user['groups'] = array();

    foreach($groups as $group) if(match_group($user['user'], $group)) {
      $user['groups'][] = $group['id'];
    }

    //check if user exist
    $replaced = false;
    $data = file('users.txt'); // reads an array of lines
    $data = array_map('replace_a_line',$data);
    file_put_contents('users.txt', implode('', $data));

    if($replaced) exit(0);

    //If user doesn't already have a key
    file_put_contents('users.txt', create_key(), FILE_APPEND | LOCK_EX);

  }
  else {
    echo 'Error getting parameter';
  }
?>
