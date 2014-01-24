package fr.pokedex;

import java.util.ArrayList;


public class Pokemon {
    public String name;
    public int number;
    
    public Type type1;
    public Type type2;
    
    public ArrayList<Talent> abilities;
    
    public int life;
    public int attack;
    public int defense;
    public int spAttack;
    public int spDefense;
    public int speed;
    
    public Pokemon(String name, int number, Type type1, Type type2,
            ArrayList<Talent> abilities, int life, int attack, int defense, int spAttack,
            int spDefense, int speed) {
        super();
        this.name = name;
        this.number = number;
        this.type1 = type1;
        this.type2 = type2;
        this.abilities = abilities;
        this.life = life;
        this.attack = attack;
        this.defense = defense;
        this.spAttack = spAttack;
        this.spDefense = spDefense;
        this.speed = speed;
    }
}
