#include <iostream>
#include <vector>
#include <fstream>

std::vector<int> load_array() {
    std::ifstream input_stream("data.txt");
    std::istream_iterator<int> start(input_stream), end;
    std::vector<int> data(start, end);
    return data;
}


int part_1() {
    std::vector<int> data = load_array();
    int result = 0;
    int val = data[0];

    for (int i: data) {
        if (i > val)
            result++;
        val = i;
    }

    return result;

}

int part_2() {
    std::vector<int> data = load_array();

    int result = 0, A, B;
    for (int i = 3; i < data.size(); i++) {
        A = data[i - 3] + data[i - 2] + data[i - 1];
        B = data[i - 2] + data[i - 1] + data[i];
        if (B > A)
            result++;
    }

    return result;
}

int main() {


    int result_part_1 = part_1();
    int result_part_2 = part_2();

    std::cout << std::string(80, '-') << std::endl;
    std::cout << "Part 1: How many measurements are larger than the previous measurement?: " << result_part_1 << std::endl;
    std::cout << std::string(80, '-') << std::endl;
    std::cout << "Part 2: How many sums are larger than the previous sum?: " << result_part_2 << std::endl;
    std::cout << std::string(80, '-') << std::endl;

}