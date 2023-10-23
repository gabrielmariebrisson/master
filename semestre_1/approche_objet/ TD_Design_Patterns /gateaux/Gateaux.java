package gateaux;

import ingredients.Ingredients;

public abstract class Gateaux implements Ingredients{
    protected String description;

    public abstract String getDescription();

    public abstract double cout();
}