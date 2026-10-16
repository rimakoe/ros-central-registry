#include <iostream>
#include <pluginlib/class_loader.hpp>
#include <urdf_parser_plugin/parser.hpp>
int main() {
    std::cout << "Loading plugin" << std::endl;
    pluginlib::ClassLoader<urdf::URDFParser> loader("urdf_parser_plugin", "urdf::URDFParser");
    std::cout << "Loaded" << std::endl;

    // std::cout << "Available plugins: " << loader.getDeclaredClasses() << std::endl;
    auto parser = loader.createSharedInstance("urdf_xml_parser/URDFXMLParser");
    std::cout << "Created" << std::endl;

    return parser ? 0 : 1;
}