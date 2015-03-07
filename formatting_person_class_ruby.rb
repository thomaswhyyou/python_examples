class Person
  GOOGLE_DIRECTORS = ["Larry Page", "Sergey Brin", "Eric Schmidt"]

  def initialize(name, age)
    @name = name
    @age = age
  end

  def say_name
    puts "Hi, my name is #{@name}."
  end

  def say_age
    puts "Hi, my age is #{@age}."
  end

  def greet_google_directors
    Person::GOOGLE_DIRECTORS.each do |name|
      puts "Hello " + name + "."
    end
  end
end

me = Person.new("thomas", 30)
me.say_name()
me.say_age()
me.greet_google_directors()
