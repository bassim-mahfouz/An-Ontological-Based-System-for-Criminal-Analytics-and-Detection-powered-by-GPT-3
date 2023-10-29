from Services import StructuredDataMapper  ,GPTInterface ,InfoExtractor,SchemaBuilder,UnStructuredDataMapper,TwitterInterface


# for structured data

# path :C:\\Users\\user\\OneDrive\\Desktop\\project\\Neo4j_Interface\\CSV
# path = input("Please enter the directory Path: ")
# value= StructuredDataMapper.integrate_csv_files_from_directory('C:\\Users\\user\\OneDrive\\Desktop\\project\\Neo4j_Interface\\CSV')

# GPTInterface.chat_with_gpt("hello bto")

# UnStructuredDataMapper.integrate_text_files_from_directory("C:\\Users\\user\\OneDrive\\Desktop\\project\\Neo4j_Interface\\Text")

# TwitterInterface.getTweets(10)

print(SchemaBuilder.buildSchema())
