from conans import ConanFile, tools
import os

required_conan_version = ">=1.43.0"


class FastFloatConan(ConanFile):
    name = "fast_float"
    description = "Fast and exact implementation of the C++ from_chars " \
                  "functions for float and double types."
    license = ("Apache-2.0", "MIT")
    topics = ("fast_float", "conversion", "from_chars")
    homepage = "https://github.com/fastfloat/fast_float"
    url = "https://github.com/conan-io/conan-center-index"

    settings = "compiler"

    no_copy_source = True

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def configure(self):
        if self.settings.compiler.get_safe("cppstd"):
            tools.check_min_cppstd(self, 11)

    def package_id(self):
        self.info.header_only()

    def source(self):
        tools.get(**self.conan_data["sources"][self.version],
                  destination=self._source_subfolder, strip_root=True)

    def package(self):
        self.copy("LICENSE*", dst="licenses", src=self._source_subfolder)
        self.copy("*", dst="include", src=os.path.join(self._source_subfolder, "include"))

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "FastFloat")
        self.cpp_info.set_property("cmake_target_name", "FastFloat::fast_float")

        self.cpp_info.names["cmake_find_package"] = "FastFloat"
        self.cpp_info.names["cmake_find_package_multi"] = "FastFloat"
        self.cpp_info.components["fastfloat"].names["cmake_find_package"] = "fast_float"
        self.cpp_info.components["fastfloat"].names["cmake_find_package_multi"] = "fast_float"
        self.cpp_info.components["fastfloat"].set_property("cmake_target_name", "FastFloat::fast_float")
