<?php

class Node
{
    public $value;
    public $namedBranches;

    public function __construct($new_item)
    {
        $this->value = $new_item;
        $this->namedBranches = [];
    }

    public function display($level)
    {
        if($level == 0) {
            var_dump(json_encode($this->namedBranches ) );
        }

        echo $this->value . "\n";
        foreach ($this->namedBranches as $b => $child_node) {
            echo str_repeat(" ", ($level + 1) * 4) . str_repeat("-", 14 / 2 - strlen($b) / 2) . $b . str_repeat("-", 14 / 2 - strlen($b) / 2) . ">";
            $child_node->display($level + 1);
        }
    }

    public function get_parent()
    {
        return ($this->tree);
    }
}
