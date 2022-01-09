#include <iostream>
#include <vector>
#include <fstream>
#include <numeric>

std::vector<int> load_array() {
    std::ifstream input_stream("data.txt");
    std::istream_iterator<int> start(input_stream), end;
    std::vector<int> data(start, end);
    return data;
}


int part_1() {
    std::vector<int> data = load_array();

    int result = 0;
    int previous_value;
    for (int value: data) {
        if (value > previous_value) {
            result++;
        }
        previous_value = value;
    }

    return result;

}

int part_2() {
    std::vector<int> data = load_array();
    int result = 0;
    int previous_value = std::accumulate(data.begin(), data.begin() + 3, 0);

    for (auto idx = data.begin() + 1; idx != data.end() - 2; idx++) {
        int value = std::accumulate(idx, idx + 3, 0);
        if (value > previous_value) {
            result++;
        }
        previous_value = value;
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