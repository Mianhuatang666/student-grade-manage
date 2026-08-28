export type StudentMap = Record<string, number>

export type StudentInput = {
    name: string
    score: number
}

export type Stats = {
    average: number
    max_score: number
    max_student: string
    min_score: number
    min_student: string
}