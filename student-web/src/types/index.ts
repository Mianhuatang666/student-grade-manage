export type StudentMap = Record<string, number>

export type StudentInput = {
    name: string
    score: number
    class_id?:number | null
}

export type Stats = {
    average: number
    max_score: number
    max_student: string
    min_score: number
    min_student: string
}

export interface ClassItem {
    id: number
    name: string
}

export type StudentWithClass = {
    name: string
    score: number
    class_name: string | null
}

export interface StudentPage {
    items: StudentWithClass[]
    total: number
    page: number
    page_size: number
}