import http  from 'k6/http';
import { sleep } from 'k6';
export default function() {
    http.get('your-url');
    sleep(0.001);
    }