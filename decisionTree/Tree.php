<?php

class Tree
{
    protected $root;

    public function __construct($root)
    {
        $this->root = $root;
    }

    public function display()
    {
        $this->root->display(0);
    }
}

